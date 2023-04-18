use pyo3::prelude::*;
use pyo3::types::PyTuple;

#[pyfunction]
fn limits_for_3_5_and_15(py: Python<'_>, input:u64) -> PyResult<&PyTuple> {
    let limit:u64 = input-1;
    let (limit3, limit5, limit15) = (limit/3, limit/5, limit/15);
    let tuple: &PyTuple;
    let elements: Vec<u64> = vec![limit3, limit5, limit15];
    tuple = PyTuple::new(py, elements);
    Ok(tuple)
}

#[pyfunction]
fn summations_for_3_5_and_15(py: Python<'_>, limit3:u64, limit5:u64, limit15:u64) -> PyResult<&PyTuple> {
    let summation3:u64 = (limit3.pow(2) + limit3)*3/2;
    let summation5:u64 = (limit5.pow(2) + limit5)*5/2;
    let summation15:u64 = (limit15.pow(2) + limit15)*15/2;
    let tuple: &PyTuple;
    let elements: Vec<u64> = vec![summation3, summation5, summation15];
    tuple = PyTuple::new(py, elements);
    Ok(tuple)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(limits_for_3_5_and_15, m)?)?;
    m.add_function(wrap_pyfunction!(summations_for_3_5_and_15, m)?)?;
    Ok(())
}
