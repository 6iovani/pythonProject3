import arcade
window = arcade.open_window(1000,900, "Graph paper")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(200,700,700,200, arcade.color.ANTIQUE_WHITE)
arcade.draw_xywh_rectangle_outline(220, 500,90,100, arcade.color.BLACK, 5 )
arcade.draw_xywh_rectangle_outline(590, 500,90,100, arcade.color.BLACK, 5 )
arcade.draw_xywh_rectangle_outline(415, 200,90,150, arcade.color.BLACK, 5 )
arcade.draw_circle_filled(900, 800, 80,arcade.color.AERO_BLUE)
arcade.draw_triangle_filled(200,700,700,700,450,800, arcade.color.BARN_RED)
arcade.draw_text("Gio's house", 100, 800, arcade.color.GOLD )
arcade.draw_arc_filled(200, 110, 100,100, arcade.color.YELLOW, 60, 330)
arcade.draw_circle_filled(250, 110, 8,arcade.color.BARN_RED)
arcade.draw_circle_filled(270, 110, 8,arcade.color.AMARANTH_PINK)
arcade.draw_circle_filled(290, 110, 8,arcade.color.BOTTLE_GREEN)


arcade.finish_render()

arcade.run()
