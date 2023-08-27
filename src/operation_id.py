def operation_id_callback(name: str, path: str, method: str) -> str:
    op_id = f'{method}_{path}'.replace('/', '_').replace('<', '').replace('>', '').replace('__', '_')
    print(op_id)
    return op_id
