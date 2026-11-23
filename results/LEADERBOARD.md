# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1172 windows, 32405 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 623 | 35.0 | 35.3 | $-341.04 | -5.5% | $658.96 | -1.0 | done | can't tell from luck |
| value_ev10 | 1532 | 38.6 | 39.2 | $-787.60 | -5.1% | $212.40 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3250 | 50.8 | 50.4 | $-1050.32 | -3.2% | $-50.32 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2735 | 49.7 | 49.4 | $-1164.20 | -4.3% | $-164.20 | -2.2 | done | losing for real |
| value_ev5 | 2320 | 40.3 | 41.1 | $-1244.08 | -5.4% | $-244.08 | -2.2 | done | losing for real |
| trend_filter | 1920 | 49.0 | 50.5 | $-1529.13 | -8.0% | $-529.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2735 | 50.3 | 51.1 | $-1708.51 | -6.2% | $-708.51 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3250 | 49.2 | 50.2 | $-1964.81 | -6.0% | $-964.81 | -3.5 | done | losing for real |
| coinflip | 4680 | 50.1 | 50.2 | $-2092.88 | -4.5% | $-1092.88 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4680 | 50.1 | 51.4 | $-2912.66 | -6.2% | $-1912.66 | -4.4 | done | losing for real |
| always_up | 4680 | 47.8 | 49.3 | $-3394.53 | -7.3% | $-2394.53 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7435 | 48.2 | 49.0 | $-3907.37 |
| ETH | 8040 | 48.1 | 48.4 | $-4761.07 |
| SOL | 8427 | 48.1 | 48.4 | $-4443.36 |
| XRP | 8503 | 48.1 | 48.2 | $-5077.97 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
