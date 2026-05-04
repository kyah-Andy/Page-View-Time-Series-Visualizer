from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot
from test_module import test_draw_line_plot, test_draw_bar_plot, test_draw_box_plot

# Generate plots
draw_line_plot()
draw_bar_plot()
draw_box_plot()

# Run tests
test_draw_line_plot()
test_draw_bar_plot()
test_draw_box_plot()

print("All tests passed successfully!")