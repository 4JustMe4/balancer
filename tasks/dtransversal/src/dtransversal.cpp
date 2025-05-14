#include <dtransversal.hpp>

#include <bitset>
#include <cassert>

namespace {
    constexpr int MAX_SQUARE_SIZE = 128;

    uint64_t transversalNumberImpl(
        const TSquare& s,
        int n,
        int row,
        std::bitset<MAX_SQUARE_SIZE>& usedNumber,
        std::bitset<MAX_SQUARE_SIZE>& usedCoulmn,
        bool hasMain,
        bool hasSub
    ) {
        if (n == row) {
            if (hasMain && hasSub) {
                return 1;
            } else {
                return 0;
            }
        }
        uint64_t ans = 0;
        for (int i = 0; i < n; i++) {
            if (hasMain && i == row)
                continue;
            if (hasSub && i + row == n - 1)
                continue;
            if (usedNumber[s[row][i]])
                continue;
            if (usedCoulmn[i])
                continue;

            usedCoulmn[i] = usedNumber[s[row][i]] = 1;
            if (i == row) hasMain = true;
            if (i + row == n - 1) hasSub = true;
            ans += transversalNumberImpl(s, n, row + 1, usedNumber, usedCoulmn, hasMain, hasSub);
            if (i == row) hasMain = false;
            if (i + row == n - 1) hasSub = false;
            usedCoulmn[i] = usedNumber[s[row][i]] = 0;
        }
        return ans;
    }
}

uint64_t transversalNumber(const TSquare& s) {
    int n = s.size();
    std::bitset<MAX_SQUARE_SIZE> usedNumber;
    std::bitset<MAX_SQUARE_SIZE> usedCoulmn;
    assert(n < MAX_SQUARE_SIZE);
    return transversalNumberImpl(s, n, 0, usedNumber, usedCoulmn, 0, 0);
}
