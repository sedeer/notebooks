import coiled

conda = {
    "channels": ["conda-forge"],
    "dependencies": [
        "dask",
        "dask-sql",
        "s3fs",
        "matplotlib",
    ],
}

# Create cluster software environment
software_name = "examples/dask-sql"
coiled.create_software_environment(
    name=software_name,
    conda=conda,
)

# Create notebook job software environment
software_notebook_name = software_name + "-notebook"
coiled.create_software_environment(
    name=software_notebook_name,
    container="coiled/notebook:latest",
    conda=conda,
    pip=["coiled==0.0.27"],
)

coiled.create_job_configuration(
    name="coiled/dask-sql",
    software=software_notebook_name,
    command=[
        "/bin/bash",
        "run.sh",
    ],
    files=["dask-sql.ipynb", "workspace.json", "run.sh"],
    ports=[8888],
    description="Query and transform Dask DataFrames using SQL",
)