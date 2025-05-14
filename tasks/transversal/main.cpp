#include <cxxopts.hpp>

#include <transversal.hpp>

#include <iostream>
#include <fstream>

int main(int argc, char* argv[]) {
    cxxopts::Options options("transversal", "Tool for transversal number calc");

    options.add_options()
        ("f,file", "Path to file with latin square", cxxopts::value<std::string>())
        ("h,help", "Show this message");

    auto result = options.parse(argc, argv);

    if (result.count("help")) {
        std::cout << options.help();
        return 0;
    }

    std::ifstream fin(result["file"].as<std::string>());
    int n;
    fin >> n;
    TSquare s(n, TSquare::value_type(n, 0));
    for (auto& u : s) {
        for (auto& w : u) {
            fin >> w;
        }
    }
    std::cout << transversalNumber(s) << std::endl;
}