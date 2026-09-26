import math

def generate_laurel(is_left=True):
    svg = '<svg viewBox="0 0 100 200" width="100%" height="100%" style="overflow: visible;">\n'
    # Stem
    stem_d = "M 50 190 Q 20 100 50 10" if is_left else "M 50 190 Q 80 100 50 10"
    svg += f'  <path d="{stem_d}" fill="none" stroke="#ccff00" stroke-width="2" stroke-linecap="round"/>\n'
    
    # Leaves
    num_leaves = 10
    for i in range(num_leaves):
        t = i / (num_leaves - 1)
        # Position along a quadratic bezier
        # P(t) = (1-t)^2 P0 + 2(1-t)t P1 + t^2 P2
        p0 = (50, 190)
        p1 = (20, 100) if is_left else (80, 100)
        p2 = (50, 10)
        
        x = (1-t)**2 * p0[0] + 2*(1-t)*t * p1[0] + t**2 * p2[0]
        y = (1-t)**2 * p0[1] + 2*(1-t)*t * p1[1] + t**2 * p2[1]
        
        # Derivative for tangent angle
        dx = 2*(1-t)*(p1[0]-p0[0]) + 2*t*(p2[0]-p1[0])
        dy = 2*(1-t)*(p1[1]-p0[1]) + 2*t*(p2[1]-p1[1])
        angle = math.degrees(math.atan2(dy, dx))
        
        # We want pairs of leaves
        for side in [-1, 1]:
            # Angle offset for leaves
            leaf_angle = angle + side * (45 if is_left else -45)
            
            # Leaf SVG path (a simple almond shape)
            leaf_path = "M 0 0 C 10 -5, 20 -5, 25 0 C 20 5, 10 5, 0 0"
            
            scale = 1.0 - (t * 0.5) # Leaves get smaller at the top
            
            svg += f'  <g class="laurel-leaf" style="transform-origin: {x}px {y}px;" data-base-angle="{leaf_angle}" data-side="{side}">\n'
            svg += f'    <path d="{leaf_path}" fill="#ccff00" transform="translate({x}, {y}) rotate({leaf_angle}) scale({scale})" />\n'
            svg += f'  </g>\n'
            
    svg += '</svg>'
    return svg

with open('laurel_left.svg', 'w') as f:
    f.write(generate_laurel(True))
with open('laurel_right.svg', 'w') as f:
    f.write(generate_laurel(False))
print("Generated SVGs")
