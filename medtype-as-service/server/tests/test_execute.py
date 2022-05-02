import pytest

from medtype_serving.server import MedTypeServer
from medtype_serving.server.helper import get_run_args

def test_execute():
    """
    A basic test to ensure that we can process some text with MedType and get back
    a bunch of results.
    """
    class Args:
        model_path = "/opt/medtype-as-service/resources/pretrained_models/pubmed_model.bin"
        type_remap_json = "/opt/medtype-as-service/config/type_remap.json"
        type2id_json = "/opt/medtype-as-service/config/type2id.json"
        umls2type_file = "/opt/medtype-as-service/resources/umls2type.pkl"
        entity_linker = "scispacy"
        http_port = "8125"

        # Need defaults
        verbose = True

    args = Args()
    with MedTypeServer(args) as server:
        server.join()