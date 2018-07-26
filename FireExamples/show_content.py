import fire


def run():
    print("running function `run()`")


def run_cli():
    # uncomment the following line to trigger example of single function called 
    # fire.Fire(run)
    
    # example of multiple function called 
    fire.Fire({
        "run": run,
        "run2": run2
    })
