import pygame
from assets.components import *
from page import *


class CustomSelectPage(Page):
    def __init__(self, screen):
        super().__init__(screen)
        self.name = "host_settings"
        self.input_data = {
            "roomID": "RoomID",
            "username": "",
            "room_password": "",
            "custom_questions": [],
        }
        self.output_data = {
            "current_page": self.name,
            "room_ID": self.input_data["roomID"],
            "username": self.input_data["username"],
            "room_password": self.input_data["room_password"],
            "exit": False
        }



    def set_components(self, screen):
        # background
        bg_img = pygame.image.load('assets/img/sky.png')
        background = Background("background", screen, bg_img)
        self.components["background"] = background

        custom_quiz_display_x = 10 / 20
        custom_quiz_display_y = 7/8
        custom_quiz_display_width = 1 / 2
        custom_quiz_display_height = 1 / 4
        custom_quiz_display_text = "Custom Questions"
        custom_quiz_display = TextDisplay("custom_questions", screen, custom_quiz_display_x, custom_quiz_display_y,
                                           custom_quiz_display_width,
                                           custom_quiz_display_height, custom_quiz_display_text)
        self.components["custom_questions"] = custom_quiz_display
        print("displayed")

        # player list
        relative_x = 4 / 20
        relative_y = 7 / 40
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 6 / 10
        shown_relative_height = 3 / 5
        custom_questions_whole = MouseScrollableSurface("custom_questions", screen, relative_x,
                                                           relative_y, relative_width,
                                                           text_relative_height, shown_relative_width,
                                                           shown_relative_height,
                                                           screen)
        # create surface
        self.components["custom_questions"] = custom_questions_whole
        self.layers.append(custom_questions_whole)

        # SelectableTextList
        relative_x = 4 / 20
        relative_y = 7 / 40
        relative_width = 0.8
        text_relative_height = 1 / 10
        shown_relative_width = 6 / 10
        shown_relative_height = 3 / 5
        custom_questions_list = self.input_data["custom_questions"]
        # print(self.input_data.keys())
        # print(custom_questions_list)

        custom_questions = SelectableTextList("custom_questions", screen, relative_x,
                                                   relative_y, relative_width,
                                                   text_relative_height, shown_relative_width, shown_relative_height,
                                                   custom_questions_list, screen, single_select=True, active_color="white")

        self.components["custom_questions"] = custom_questions
        custom_questions_whole.add_component(custom_questions)
        self.layers.append(custom_questions)

        # return button
        return_button2_x = 1 / 20
        return_button2_y = 17 / 20
        return_button2_width = 1 / 10
        return_button2_height = 1 / 10
        return_button2__img = pygame.image.load('assets/img/exit_btn.png')
        return_button2 = ImageButton("return_button", screen, return_button2_x, return_button2_y,
                                    return_button2_width,
                                    return_button2_height, return_button2__img)
        self.components["return_button"] = return_button2

        # confirm button
        confirm_button_x = 17 / 20
        confirm_button_y = 17 / 20
        confirm_button_width = 1 / 10
        confirm_button_height = 1 / 10
        confirm_button__img = pygame.image.load('assets/img/save_btn.png')
        confirm_button2 = ImageButton("confirm_button", screen, confirm_button_x, confirm_button_y,
                                    confirm_button_width,
                                    confirm_button_height, confirm_button__img)
        self.components["confirm_button"] = confirm_button2

        # how do the page react to events?
    def page_function(self, triggered_component_list):
        for triggered_component in triggered_component_list:
            if triggered_component in [self.components["return_button2"]]:
                self.name = "host_settings"
            if triggered_component in [self.components["confirm_button2"]]:
                print("Go to custom quiz creation page")