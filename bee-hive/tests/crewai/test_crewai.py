#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0

from unittest import TestCase
import dotenv
import os
import yaml

from bee_hive import Workflow

dotenv.load_dotenv()

# TODO: consider moving setup here
# @pytest.fixture(scope="module")


class CrewAITest(TestCase):

    def test_agent_runs(self) -> None:
        def parse_yaml(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                yaml_data = list(yaml.safe_load_all(file))
            return yaml_data

        agents_yaml = parse_yaml(os.path.join(os.path.dirname(__file__),"agents.yaml"))
        workflow_yaml = parse_yaml(os.path.join(os.path.dirname(__file__),"workflow.yaml"))
        try:
            workflow = Workflow(agents_yaml, workflow_yaml[0])
        except Exception as excep:
            raise RuntimeError("Unable to create agents") from excep
        result = workflow.run()
        print(result)

        assert result is not None
        assert result["final_prompt"] == "OK"
