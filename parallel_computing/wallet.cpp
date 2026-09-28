#include <iostream>
#include <thread>
#include <vector>
#include <functional>
#include <mutex>

class CWallet
{
public:
    CWallet() : m_Money(0) {}

    int getMoney() { return m_Money; }

    void addMoneyWithMutex(int vMoney)
    {
        m_Mutex.lock();
        for (int i = 0; i < vMoney; ++i)
        {
            m_Money++;
        }
        m_Mutex.unlock();
    }

    void addMoneyWithLockGuard(int vMoney)
    {
        std::lock_guard<std::mutex> Guard(m_Mutex);
        for (int i = 0; i < vMoney; ++i)
        {
            m_Money++;
        }
    }

private:
    int m_Money;
    std::mutex m_Mutex;
};

using AddMoneyOperation = std::function<void(CWallet&, int)>;

int testMultithreadedWallet(int vNumThread, int vMoney, AddMoneyOperation operation)
{
    CWallet WalletObject;
    std::vector<std::thread> ThreadSet;

    for (int i = 0; i < vNumThread; ++i)
    {
        ThreadSet.emplace_back(operation, std::ref(WalletObject), vMoney);
    }

    for (auto& thread : ThreadSet)
    {
        thread.join();
    }

    return WalletObject.getMoney();
}

int main()
{
    //testMultithreadedWallet(5, 1000, &CWallet::addMoneyWithMutex);
    //testMultithreadedWallet(5, 1000, &CWallet::addMoneyWithLockGuard);

    return 0;
}
