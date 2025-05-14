#include "boinc_api.h"

#include <transversal.hpp>

#include <iostream>
#include <fstream>


namespace {
    constexpr int MAX_FILENAME_LENGTH = 1024;
    TSquare readInput() {
        char resolved_input[MAX_FILENAME_LENGTH];
        int retval = boinc_resolve_filename("input.txt", resolved_input, sizeof(resolved_input));
        if (retval) {
            boinc_finish(1);
            exit(1);
        }

        std::ifstream fin(resolved_input);
        if (!fin) {
            boinc_finish(2);
            exit(2);
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
        int retval = boinc_resolve_filename("output.txt", resolved_output, sizeof(resolved_output));
        if (retval) {
            boinc_finish(3); // Ошибка: не найден выходной файл
            exit(3);
        }
        std::ofstream fout(resolved_output);
        fout << result << std::endl;
        fout.close();
    }
}

int main(int argc, char* argv[]) {
    boinc_init();

    auto s = readInput();
    auto result = transversalNumber(s);
    writeOutput(result);
    
    boinc_finish(0);
}