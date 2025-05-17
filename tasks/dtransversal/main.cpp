#include "boinc_api.h"

#include <dtransversal.hpp>

#include <iostream>
#include <fstream>


namespace {
    constexpr int MAX_FILENAME_LENGTH = 1024;
    TSquare readInput() {
        char resolved_input[MAX_FILENAME_LENGTH];
        int retval = boinc_resolve_filename("in", resolved_input, sizeof(resolved_input));
        if (retval) {
            std::cerr << "Can't resolve input file" << std::endl;
            boinc_finish(1);
            return {};
        }
        std::cerr << "Input file is: " << resolved_input << std::endl;
        std::ifstream fin(resolved_input);
        if (!fin) {
            std::cerr << "Can't open input " << resolved_input << std::endl;
            boinc_finish(2);
            return {};
        }
        int n;
        fin >> n;
        TSquare s(n, TSquare::value_type(n, 0));
        for (auto& u : s) {
            for (auto& w : u) {
                fin >> w;
            }
        }
        fin.close();
        return s;
    }

    void writeOutput(uint64_t result) {
        char resolved_output[MAX_FILENAME_LENGTH];
        int retval = boinc_resolve_filename("out", resolved_output, sizeof(resolved_output));
        if (retval) {
            std::cerr << "Can't open output file " << std::endl;
            boinc_finish(3);
            return;
        }
        std::ofstream fout(resolved_output);
        fout << result << std::endl;
        fout.close();
    }
}

int main(int argc, char* argv[]) {
    boinc_init();

    auto s = readInput();
    auto result = dtransversalNumber(s);
    writeOutput(result);
    
    boinc_finish(0);
}
