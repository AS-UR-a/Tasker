import flet as ft

@ft.control
class TodoApp(ft.Column):
    def init(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.task_view = ft.Column()
        self.width = 600

        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    ft.FloatingActionButton
                    (
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            self.task_view
        ]

    def add_clicked(self, e):
        self.task_view.controls.append(ft.Checkbox(label=self.new_task.value))
        new_task.value = ""
        self.update()



def main(page: ft.Page):
    page.title = "Tasker"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()
    page.add(todo)

ft.run(main)