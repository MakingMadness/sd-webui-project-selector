import gradio as gr
import os

from modules import script_callbacks
from modules.shared import opts

def get_project_dirs():
    if os.path.isdir(opts.projects_path):
        return sorted([d for d in os.listdir(opts.projects_path) if os.path.isdir(os.path.join(opts.projects_path, d))])
    else:
        return []

def report_outdirs():
    return f"""txt2img samples: {opts.outdir_txt2img_samples}
img2img samples: {opts.outdir_img2img_samples}
txt2img grids: {opts.outdir_txt2img_grids}
img2img grids: {opts.outdir_img2img_grids}
extras samples: {opts.outdir_extras_samples}
save: {opts.outdir_save}"""

def update_outdirs(project_name):
    if project_name:
        if not os.path.isdir(opts.projects_path):
            os.mkdir(opts.projects_path)
        project_dir = os.path.join(opts.projects_path, project_name) if project_name else opts.projects_path
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        if original_outdir_samples:
            opts.set("outdir_samples", "")
        opts.set("outdir_txt2img_samples", os.path.join(project_dir, opts.projects_txt2img_samples_suffix))
        opts.set("outdir_img2img_samples", os.path.join(project_dir, opts.projects_img2img_samples_suffix))
        opts.set("outdir_grids", "")
        opts.set("outdir_txt2img_grids", os.path.join(project_dir, opts.projects_txt2img_grids_suffix))
        opts.set("outdir_img2img_grids", os.path.join(project_dir, opts.projects_img2img_grids_suffix))
        opts.set("outdir_extras_samples", os.path.join(project_dir, opts.projects_extras_samples_suffix))
        opts.set("outdir_save", os.path.join(project_dir, opts.projects_save_suffix))
    return report_outdirs()

def create_new_project(project_name):
    output = update_outdirs(project_name)
    return [ 
      gr.Dropdown.update(
        choices = get_project_dirs(),
        value = project_name
       ), 
       gr.Textbox.update(value = output) 
    ]

def reset_outdirs():
    opts.set("outdir_samples", original_outdir_samples)
    opts.set("outdir_txt2img_samples", original_outdir_txt2img_samples)
    opts.set("outdir_img2img_samples", original_outdir_img2img_samples)
    opts.set("outdir_grids", original_outdir_grids)
    opts.set("outdir_txt2img_grids", original_outdir_txt2img_grids)
    opts.set("outdir_img2img_grids", original_outdir_img2img_grids)
    opts.set("outdir_extras_samples", original_outdir_extras_samples)
    opts.set("outdir_save", original_outdir_save)
    return [ 
      gr.Dropdown.update(
        value = ""
       ), 
       gr.Textbox.update(value = report_outdirs()) 
    ]

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:

        with gr.Row():
            project_output = gr.Textbox(
                label="Current Output Paths",
                readonly=True,
                disabled=True,
                lines=6,
                value=report_outdirs()
            )

        with gr.Row():
            project_dropdown = gr.Dropdown(
                get_project_dirs(), 
                label="Selected Project",
                allow_custom_value=False
            )
            project_dropdown.change(update_outdirs, inputs=project_dropdown, outputs=[project_output])

        with gr.Row():
            new_project_button = gr.Button(
                value="Deselect Project"
            )
            new_project_button.click(reset_outdirs, outputs=[project_dropdown, project_output])

        with gr.Row():
            with gr.Column(scale=3):
                new_project_textbox = gr.Textbox(
                    label="New Project",
                    lines=1
                )
            with gr.Column(scale=1):
                new_project_button = gr.Button(
                    label=" ",
                    value="Create"
                )
                new_project_button.click(create_new_project, inputs=[new_project_textbox], outputs=[project_dropdown, project_output])

        return [(ui_component, "Project", "project_selector_tab")]

original_outdir_samples = opts.outdir_samples
original_outdir_txt2img_samples = opts.outdir_txt2img_samples
original_outdir_img2img_samples = opts.outdir_img2img_samples
original_outdir_grids = opts.outdir_grids
original_outdir_txt2img_grids = opts.outdir_txt2img_grids
original_outdir_img2img_grids = opts.outdir_img2img_grids
original_outdir_extras_samples = opts.outdir_extras_samples
original_outdir_save = opts.outdir_save

script_callbacks.on_ui_tabs(on_ui_tabs)