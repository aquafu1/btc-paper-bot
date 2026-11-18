# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 6:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 667 windows, 18441 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 344 | 34.3 | 35.3 | $-242.35 | -7.0% | $757.65 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1569 | 50.4 | 49.6 | $-437.28 | -2.8% | $562.72 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 1891 | 51.5 | 50.9 | $-568.06 | -3.0% | $431.94 | -1.3 | done | can't tell from luck |
| trend_filter | 1072 | 50.4 | 50.9 | $-570.94 | -5.3% | $429.06 | -1.8 | done | can't tell from luck |
| value_ev10 | 845 | 38.2 | 39.5 | $-605.91 | -7.2% | $394.09 | -1.7 | done | can't tell from luck |
| value_ev5 | 1277 | 40.6 | 41.4 | $-721.27 | -5.6% | $278.73 | -1.7 | done | can't tell from luck |
| coinflip | 2661 | 50.1 | 50.4 | $-1210.81 | -4.6% | $-210.81 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1569 | 49.6 | 51.3 | $-1225.32 | -7.8% | $-225.32 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 1891 | 48.5 | 50.1 | $-1311.76 | -6.9% | $-311.76 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2661 | 50.8 | 51.8 | $-1423.60 | -5.3% | $-423.60 | -2.9 | done | losing for real |
| always_up | 2661 | 47.5 | 49.7 | $-2232.83 | -8.4% | $-1232.83 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4190 | 48.3 | 49.3 | $-2608.68 |
| ETH | 4606 | 48.3 | 48.6 | $-2755.11 |
| SOL | 4800 | 48.2 | 48.8 | $-2844.63 |
| XRP | 4845 | 48.6 | 48.6 | $-2341.72 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
