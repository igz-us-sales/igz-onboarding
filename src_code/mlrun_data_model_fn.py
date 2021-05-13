from tensorflow.keras.models import load_model

def handler(context):
    ########################
    ####### Model ##########
    ########################
    # "Train" model (load from disk)
    model_dir = context.get_input("model")
    model = load_model(str(model_dir))
    
    # Save "trained" model to artifact path
    model.save("model.h5")
    
    # Log model to DB
    context.logger.info("Logging model")
    context.log_model(
        key="my_model",
        artifact_path=context.artifact_path,
        model_file="model.h5",
        metrics={"loss" : 0.23, "accuracy" : 0.94},
        tag="latest",
        parameters={
            "batch_size" : 64,
            "epochs" : 10
        },
        framework="keras",
        labels={"notes" : "noted"},
    )
    
    ########################
    ######### CSV ##########
    ########################
    # Load CSV as dataframe from input
    df = context.get_input("csv").as_df()
    
    # Log CSV to DB
    context.logger.info("Logging CSV")
    context.log_dataset(
        key="my_csv",
        df=df,
        format="csv",
        artifact_path=context.artifact_path
    )