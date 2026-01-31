from dataclasses import field
from typing import Callable

import flet as ft 

@ft.control
class Task(ft.Column):
    task_name = ""
    on_task_delete: Callable[[Task], None] = field(default=lambda task: None)

    def init(self):
        self.display_task = ft.Checkbox(value=False, label=self.task_name)
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            aligment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_aligment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.display_task,
                ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                        ),
                        ft.IconButton(

                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(

        )
        self.controls = []

    def edit_clicked(self, e):

    def save_clicked(self, e):

    def delete_clicked(self, e):


@ft.control
class TodoApp(ft.Column):
    def init(self):






def main(page: ft.Page):




ft.run(main)