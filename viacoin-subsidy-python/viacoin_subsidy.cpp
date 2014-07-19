#include <Python.h>

static const int64_t COIN = 100000000;

static int64_t GetBlockBaseValue(int nHeight, bool fTestNet = false)
{
    int64_t nSubsidy = 0;
    int tHeight = 5256000; // reduction frequency: 3600 * 365 * 4

    // different zero block period for testnet and mainnet
    // mainnet not fixed until final release
    int zeroRewardHeight = fTestNet ? 2001 : 10001;

    int rampHeight = 43200 + zeroRewardHeight; // 4 periods of 10800

    if (nHeight == 0) {
        // no reward for genesis block
        nSubsidy = 0;
    } else if (nHeight == 1) {
        // first distribution
        nSubsidy = 10000000 * COIN;
    } else if (nHeight <= zeroRewardHeight) {
        // no block reward to allow difficulty to scale up and prevent instamining
        nSubsidy = 0;
    } else if (nHeight <= (zeroRewardHeight + 10800)) {
        // first 10800 block after zero reward period is 10 coins per block
        nSubsidy = 10 * COIN;
    } else if (nHeight <= rampHeight) {
        // every 10800 blocks reduce nSubsidy from 8 to 6
        nSubsidy = (8 - int((nHeight-zeroRewardHeight-1) / 10800)) * COIN;
    } else if (nHeight <= tHeight) {
        // first 4 years
        nSubsidy = 5 * COIN;
    } else if (nHeight <= (2 * tHeight)) {
        // next 4 years
        nSubsidy = 4 * COIN;
    } else if (nHeight <= (3 * tHeight)) {
        // next 4 years
        nSubsidy = 3 * COIN;
    } else if (nHeight <= (4 * tHeight)) {
        // next 4 years
        nSubsidy = 2 * COIN;
    } else if (nHeight <= (5 * tHeight)) {
        // next 4 years
        nSubsidy = 1 * COIN;
    } else if (nHeight <= (6 * tHeight)) {
        // next 4 years
        nSubsidy = 0.5 * COIN;
    }

    return nSubsidy;
}

static PyObject *viacoin_subsidy_getblockbasevalue(PyObject *self, PyObject *args)
{
    int input_height;
    if (!PyArg_ParseTuple(args, "i", &input_height))
        return NULL;
    long long output = GetBlockBaseValue(input_height);
    return Py_BuildValue("L", output);
}

static PyObject *viacoin_subsidy_getblockbasevalue_testnet(PyObject *self, PyObject *args)
{
    int input_height;
    if (!PyArg_ParseTuple(args, "i", &input_height))
        return NULL;
    long long output = GetBlockBaseValue(input_height, true);
    return Py_BuildValue("L", output);
}

static PyMethodDef viacoin_subsidy_methods[] = {
    { "getBlockBaseValue", viacoin_subsidy_getblockbasevalue, METH_VARARGS, "Returns the block value" },
    { "getBlockBaseValue_testnet", viacoin_subsidy_getblockbasevalue_testnet, METH_VARARGS, "Returns the block value for testnet" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initviacoin_subsidy(void) {
    (void) Py_InitModule("viacoin_subsidy", viacoin_subsidy_methods);
}
