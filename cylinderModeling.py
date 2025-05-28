import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from matplotlib.patches import Circle, FancyBboxPatch
from mpl_toolkits.mplot3d import Axes3D


def segment_area(R, h):
    """Calculate the area of circular segment given radius R and height h"""
    if h >= 2 * R:
        return np.pi * R ** 2
    if h <= 0:
        return 0

    theta = 2 * np.arccos((R - h) / R)
    area = (R ** 2 * (theta - np.sin(theta))) / 2
    return area


def find_height_for_volume_ratio(R, L, target_ratio):
    """Find height h that gives target_ratio of total volume"""
    total_volume = np.pi * R ** 2 * L
    target_volume = total_volume * target_ratio

    def volume_difference(h):
        return segment_area(R, h) * L - target_volume

    initial_guess = R
    h = fsolve(volume_difference, initial_guess)[0]
    return h


def plot_enhanced_cylinder(R, L, h):
    """Create an enhanced visualization of the cylinder with water"""
    # Use a built-in style instead of seaborn
    plt.style.use('default')

    # Create figure with 3 subplots
    fig = plt.figure(figsize=(15, 5))
    fig.patch.set_facecolor('white')  # Set white background

    fig.suptitle('Horizontal Cylinder Water Level Visualization',
                 fontsize=16, fontweight='bold', y=1.05)

    # Side view (enhanced)
    ax1 = fig.add_subplot(131)
    # Draw cylinder outline
    rect = FancyBboxPatch((0, 0), 2 * R, 2 * R, boxstyle="round,pad=0",
                          facecolor='none', edgecolor='black', linewidth=2)
    ax1.add_patch(rect)

    # Draw water
    ax1.fill_between([0, 2 * R], [0] * 2, [h] * 2, color='lightblue', alpha=0.6)
    ax1.plot([0, 2 * R], [h, h], 'b-', linewidth=2)

    # Styling
    ax1.set_xlim(-0.2 * R, 2.2 * R)
    ax1.set_ylim(-0.2 * R, 2.2 * R)
    ax1.set_aspect('equal')
    ax1.set_title('Side View', pad=10, fontsize=12, fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.set_xlabel('Length', fontsize=10)
    ax1.set_ylabel('Height', fontsize=10)

    # End view (enhanced)
    ax2 = fig.add_subplot(132)
    circle = Circle((R, R), R, fill=False, linewidth=2)
    ax2.add_artist(circle)

    # Calculate and plot water surface
    theta = np.arccos((R - h) / R)
    x = R + R * np.cos(np.linspace(-theta, theta, 100))
    y = h + np.zeros_like(x)

    # Fill water region
    ax2.fill_between(x, np.zeros_like(x), y, color='lightblue', alpha=0.6)
    ax2.plot(x, y, 'b-', linewidth=2)

    # Styling
    ax2.set_xlim(-0.2 * R, 2.2 * R)
    ax2.set_ylim(-0.2 * R, 2.2 * R)
    ax2.set_aspect('equal')
    ax2.set_title('End View', pad=10, fontsize=12, fontweight='bold')
    ax2.grid(True, linestyle='--', alpha=0.7)
    ax2.set_xlabel('Width', fontsize=10)
    ax2.set_ylabel('Height', fontsize=10)

    # 3D visualization
    ax3 = fig.add_subplot(133, projection='3d')

    # Create cylinder points
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, L, 50)
    theta, z = np.meshgrid(theta, z)
    x = R * np.cos(theta)
    y = R * np.sin(theta)

    # Plot cylinder surface with lighter gray color
    ax3.plot_surface(x, y, z, alpha=0.3, color='lightgray')

    # Calculate water surface for 3D
    theta_water = np.linspace(-np.arccos((R - h) / R), np.arccos((R - h) / R), 100)
    z_water = np.linspace(0, L, 50)
    theta_water, z_water = np.meshgrid(theta_water, z_water)
    x_water = R * np.cos(theta_water)
    y_water = R * np.sin(theta_water)
    water_level = np.full_like(x_water, h)

    # Plot water surface with enhanced color
    ax3.plot_surface(x_water, y_water, z_water, color='lightblue', alpha=0.6)

    # Styling
    ax3.set_title('3D View', pad=10, fontsize=12, fontweight='bold')
    ax3.set_xlabel('Width', fontsize=10)
    ax3.set_ylabel('Depth', fontsize=10)
    ax3.set_zlabel('Length', fontsize=10)
    ax3.view_init(elev=20, azim=45)

    # Add timestamp and info
    current_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    plt.figtext(0.02, 0.02, f"Generated: {current_utc}",
                fontsize=8, style='italic')

    # Add volume information
    volume_text = f"Volume Ratio: {target_ratio:.0%}\nHeight: {h:.4f} units"
    plt.figtext(0.02, 0.95, volume_text, fontsize=10)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Parameters
    R = 1.0  # Radius
    L = 3.0  # Length
    target_ratio = 1 / 4  # Target volume ratio

    # Calculate height
    h = find_height_for_volume_ratio(R, L, target_ratio)

    # Print results with UTC timestamp
    current_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Current Date and Time (UTC): {current_utc}")
    print(f"\nCylinder Parameters:")
    print(f"Radius (R) = {R} units")
    print(f"Length (L) = {L} units")
    print(f"Target Fill Ratio = {target_ratio:.0%}")
    print(f"Calculated Height (h) = {h:.4f} units")

    # Create enhanced visualization
    plot_enhanced_cylinder(R, L, h)