from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="imaginAIry",
    author="Bryce Drennan",
    author_email="b r y p y d o t io",
    version="0.7.0",
    description="AI imagined images. Pythonic generation of stable diffusion images.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=find_packages(include=("imaginairy", "imaginairy.*")),
    entry_points={
        "console_scripts": ["imagine=imaginairy.cmd_wrap:imagine_cmd"],
    },
    package_data={"imaginairy": ["configs/*.yaml"]},
    install_requires=[
        "click",
        "torch",
        "numpy",
        "tqdm",
        "diffusers",
        "imageio==2.9.0",
        "pytorch-lightning==1.4.2",
        "omegaconf==2.1.1",
        "einops==0.3.0",
        "transformers==4.19.2",
        "torchmetrics==0.6.0",
        "torchvision>=0.13.1",
        "kornia==0.6",
        "clip @  git+https://github.com/openai/CLIP",
        # k-diffusion for use with find_noise.py
        # "k-diffusion@git+https://github.com/crowsonkb/k-diffusion.git@71ba7d6735e9cba1945b429a21345960eb3f151c#egg=k-diffusion",
    ],
)
