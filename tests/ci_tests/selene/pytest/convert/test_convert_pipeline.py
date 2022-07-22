import os

CI_JOB_RESULTS = os.environ.get("RESULTS_DIR")  #eg '/home/shanmugamr/bignlp-scripts/results/train_gpt3_126m_tp1_pp1_1node_100steps'

class TestConvertPipeline:

    job_name = CI_JOB_RESULTS_DIR.rsplit("/",1)[1] #eg train_gpt3_126m_tp1_pp1_1node_100steps
    model = job_name.split("_")[1] #eg gpt3
    if model == "gpt3":
        model = "gpt" # Should get this addressed
    output_file="megatron" + model + ".nemo"

    def test_ci_convert(self):
        ckpt_path = os.path.join(CI_JOB_RESULTS, self.output_file)
        assert os.path.exists(ckpt_path), f"File not found: {ckpt_path}"
