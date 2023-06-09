import gradio as gr
import os

from modules import shared
from modules import script_callbacks

def on_ui_settings():
    section = ('project_selector', "Project Selector")

    shared.opts.add_option(
        "projects_path",
        shared.OptionInfo(
            "projects" + os.path.sep,
            "Projects Path",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_txt2img_samples_suffix",
        shared.OptionInfo(
            shared.opts.outdir_txt2img_samples,
            "txt2img Samples Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_img2img_samples_suffix",
        shared.OptionInfo(
            shared.opts.outdir_img2img_samples,
            "img2img Samples Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_txt2img_grids_suffix",
        shared.OptionInfo(
            shared.opts.outdir_txt2img_grids,
            "txt2img Grids Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_img2img_grids_suffix",
        shared.OptionInfo(
            shared.opts.outdir_img2img_grids,
            "img2img Grids Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_extras_samples_suffix",
        shared.OptionInfo(
            shared.opts.outdir_extras_samples,
            "Extras Samples Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "projects_save_suffix",
        shared.OptionInfo(
            shared.opts.outdir_save,
            "Save Path Suffix",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_samples",
        shared.OptionInfo(
            shared.opts.outdir_samples,
            "Original Outdir Samples",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_txt2img_samples",
        shared.OptionInfo(
            shared.opts.outdir_txt2img_samples,
            "Original Outdir Txt2img Samples",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_img2img_samples",
        shared.OptionInfo(
            shared.opts.outdir_img2img_samples,
            "Original Outdir Img2img Samples",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_grids",
        shared.OptionInfo(
            shared.opts.outdir_grids,
            "Original Outdir Grids",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_txt2img_grids",
        shared.OptionInfo(
            shared.opts.outdir_txt2img_grids,
            "Original Outdir Txt2img Grids",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_img2img_grids",
        shared.OptionInfo(
            shared.opts.outdir_img2img_grids,
            "Original Outdir Img2img Grids",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_extras_samples",
        shared.OptionInfo(
            shared.opts.outdir_extras_samples,
            "Original Outdir Extras Samples",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

    shared.opts.add_option(
        "original_outdir_save",
        shared.OptionInfo(
            shared.opts.outdir_save,
            "Original Outdir Save",
            gr.Textbox,
            {"lines": 1, "interactive": True},
            section=section)
    )

script_callbacks.on_ui_settings(on_ui_settings)
