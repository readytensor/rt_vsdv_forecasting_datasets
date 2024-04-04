from generate_schemas import run_schema_gen
from create_variations import generate_variations
from create_train_test_key_files import run_train_test_testkey_files_gen
from validator import validate_all

if __name__ == "__main__":
    run_schema_gen()
    generate_variations()
    run_train_test_testkey_files_gen()
    validate_all()
