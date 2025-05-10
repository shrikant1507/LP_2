#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric> 

using namespace std;

struct StockData {
    double closingPrice;
    double volume;
    double eps;
    double peRatio;
    double debtToEquity;
    double beta;
    double standardDeviation;
    double sharpeRatio;
    double var;
    string newsSentiment;
};

double calculateEPS(double netIncome, double preferredDividends, double outstandingShares) {
    return (netIncome - preferredDividends) / outstandingShares;
}

double calculateBeta(const vector<double>& stockReturns, const vector<double>& marketReturns) {
    double stockMean = accumulate(stockReturns.begin(), stockReturns.end(), 0.0) / stockReturns.size();
    double marketMean = accumulate(marketReturns.begin(), marketReturns.end(), 0.0) / marketReturns.size();

    double numerator = 0.0, denominator = 0.0;
    for (size_t i = 0; i < stockReturns.size(); i++) {
        numerator += (stockReturns[i] - stockMean) * (marketReturns[i] - marketMean);
        denominator += (marketReturns[i] - marketMean) * (marketReturns[i] - marketMean);
    }

    return numerator / denominator;
}

StockData getStockData() {
    StockData sd;
    cout << "Enter the closing price: ";
    cin >> sd.closingPrice;
    cout << "Enter the trading volume: ";
    cin >> sd.volume;

    double netIncome, preferredDividends, outstandingShares;
    cout << "Enter the net income: ";
    cin >> netIncome;
    cout << "Enter the preferred dividends: ";
    cin >> preferredDividends;
    cout << "Enter the average outstanding shares: ";
    cin >> outstandingShares;
    sd.eps = calculateEPS(netIncome, preferredDividends, outstandingShares);
    cout << "Earnings Per Share (EPS): " << sd.eps << endl;

    cout << "Enter the P/E ratio: ";
    cin >> sd.peRatio;
    cout << "Enter the debt-to-equity ratio: ";
    cin >> sd.debtToEquity;

    cout << "Enter the standard deviation of the stock: ";
    cin >> sd.standardDeviation;
    cout << "Standard Deviation: " << sd.standardDeviation << endl;

    vector<double> stockReturns, marketReturns;
    int numReturns;
    cout << "Enter the number of return periods: ";
    cin >> numReturns;
    cout << "Enter the stock returns: ";
    for (int i = 0; i < numReturns; i++) {
        double returnValue;
        cin >> returnValue;
        stockReturns.push_back(returnValue);
    }
    cout << "Enter the market returns: ";
    for (int i = 0; i < numReturns; i++) {
        double returnValue;
        cin >> returnValue;
        marketReturns.push_back(returnValue);
    }
    sd.beta = calculateBeta(stockReturns, marketReturns);
    cout << "Beta: " << sd.beta << endl;

    cout << "Enter the Sharpe ratio: ";
    cin >> sd.sharpeRatio;
    cout << "Enter the Value at Risk (VaR): ";
    cin >> sd.var;
    cout << "Enter the news sentiment (positive/negative/neutral): ";
    cin >> sd.newsSentiment;

    return sd;
}

void analyzeStockData(const StockData& sd) {
    string recommendation;
    if (sd.beta > 1.0 && sd.standardDeviation > 0.05) {
        recommendation = "High Risk: The stock is highly volatile and risky. Consider investing with caution.";
    } else if (sd.peRatio < 15 && sd.sharpeRatio > 1.0) {
        recommendation = "Moderate Risk: The stock has a good risk-adjusted return. Consider investing.";
    } else {
        recommendation = "Low Risk: The stock is stable and has low volatility. Consider investing.";
    }

    cout << "Recommendation: " << recommendation << endl;
}

int main() {
    cout << "Welcome to the Stock Recommendation System" << endl;

    StockData sd = getStockData();
    analyzeStockData(sd);

    return 0;
}
