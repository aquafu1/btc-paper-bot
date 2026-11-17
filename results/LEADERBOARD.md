# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 589 windows, 16302 settled trades, 51 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1386 | 51.2 | 49.6 | $-199.29 | -1.4% | $800.71 | -0.5 | done | can't tell from luck |
| value_ev20 | 321 | 34.0 | 35.2 | $-276.40 | -8.6% | $723.60 | -1.2 | done | can't tell from luck |
| trend_filter | 946 | 50.3 | 50.9 | $-524.37 | -5.5% | $475.63 | -1.7 | done | can't tell from luck |
| value_ev10 | 766 | 37.9 | 39.4 | $-625.17 | -8.2% | $374.83 | -1.9 | done | can't tell from luck |
| value_ev5 | 1145 | 40.4 | 41.3 | $-704.66 | -6.2% | $295.34 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1654 | 50.7 | 51.0 | $-841.63 | -5.1% | $158.37 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1654 | 49.3 | 49.9 | $-899.40 | -5.4% | $100.60 | -2.2 | done | losing for real |
| coinflip | 2348 | 49.9 | 50.5 | $-1204.97 | -5.1% | $-204.97 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1386 | 48.8 | 51.3 | $-1355.19 | -9.8% | $-355.19 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2348 | 50.2 | 51.8 | $-1613.91 | -6.9% | $-613.91 | -3.5 | done | losing for real |
| always_up | 2348 | 47.4 | 49.8 | $-2090.04 | -8.9% | $-1090.04 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3700 | 47.9 | 49.2 | $-2529.86 |
| ETH | 4067 | 48.1 | 48.6 | $-2584.87 |
| SOL | 4239 | 47.9 | 48.7 | $-2963.01 |
| XRP | 4296 | 48.5 | 48.6 | $-2257.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
