import reflex as rx


class TaskState(rx.State):
    name : str = ''
    description : str = ''
    form_data: dict = {}
    def clear_text(self):
        self.name = ''
        self.description = ''
    
    def handle_submit(self, form_data):
       self.form_data = form_data
       print(self.name, self.description)
       return [
            rx.set_value(field_id, "")
            for field_id in form_data
        ]
  

def form():
    return  rx.container(
        rx.form(
            rx.vstack(
            # Task name input
                rx.input(
                    value=TaskState.name,
                    on_change=TaskState.set_name,
                    placeholder='Task name',
                    type_='text',
                    
                ),

                # Task description input
                rx.text_area(
                    value=TaskState.description,
                    on_change=TaskState.set_description,
                    placeholder='Task description',

                ),

                rx.box(
                    # Submit button
                    rx.button(
                        'Add Task',
                        type_='submit',
                        bg='#4f45e1',
                        color='white',
                        border_radius='10px',
                        padding='0.5em 1em',
                       
                    ),
                    # Clear button
                    rx.button(
                        'Reset',
                        on_click= TaskState.clear_text,

                    )
                ),
                
        ),
        on_submit=TaskState.handle_submit  
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(TaskState.form_data.to_string()),
    )