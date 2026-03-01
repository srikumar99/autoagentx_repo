from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="autoagentx",
    version="1.0.0",
    author="Jordan R. Mitchell et al.",
    author_email="jrmitchell@cs.stanford.edu",
    description="AutoAgent-X: Hierarchical Goal-Decomposition for Autonomous Multi-Step Task Execution",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/autoagentx/autoagentx",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=[
        "openai>=1.10.0",
        "anthropic>=0.18.0",
        "pyyaml>=6.0",
        "pydantic>=2.0",
        "networkx>=3.1",         # DAG construction and traversal
        "tenacity>=8.2",         # Retry logic for API calls
        "rich>=13.0",            # Pretty terminal output
        "httpx>=0.24.0",
        "tiktoken>=0.5.0",
    ],
    extras_require={
        "memory": [
            "faiss-cpu>=1.7.4",
            "sentence-transformers>=2.2.2",
            "numpy>=1.24.0",
        ],
        "full": [
            "faiss-cpu>=1.7.4",
            "sentence-transformers>=2.2.2",
            "numpy>=1.24.0",
            "torch>=2.0.0",
            "transformers>=4.35.0",
            "datasets>=2.14.0",
            "matplotlib>=3.7.0",
            "pandas>=2.0.0",
            "scipy>=1.11.0",
        ],
        "dev": [
            "pytest>=7.4.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.4.0",
            "ruff>=0.0.280",
        ],
    },
    entry_points={
        "console_scripts": [
            "autoagentx=autoagentx.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
