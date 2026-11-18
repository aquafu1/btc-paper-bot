# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 4:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 752 windows, 20769 settled trades, 36 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 393 | 33.8 | 34.9 | $-281.45 | -7.2% | $718.55 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 2122 | 51.5 | 50.5 | $-485.80 | -2.3% | $514.20 | -1.1 | done | can't tell from luck |
| value_ev10 | 953 | 38.0 | 39.1 | $-606.39 | -6.4% | $393.61 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 1755 | 50.0 | 49.6 | $-666.23 | -3.8% | $333.77 | -1.6 | done | can't tell from luck |
| value_ev5 | 1437 | 40.4 | 41.1 | $-775.44 | -5.4% | $224.56 | -1.7 | done | can't tell from luck |
| trend_filter | 1223 | 49.8 | 50.9 | $-813.12 | -6.6% | $186.88 | -2.4 | done | losing for real |
| coinflip | 3003 | 50.4 | 50.2 | $-1102.02 | -3.7% | $-102.02 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 1755 | 50.0 | 51.2 | $-1193.34 | -6.8% | $-193.34 | -2.9 | done | losing for real |
| momentum_15m_0.10pct | 2122 | 48.5 | 50.2 | $-1550.50 | -7.3% | $-550.50 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 3003 | 50.8 | 51.8 | $-1646.71 | -5.5% | $-646.71 | -3.1 | done | losing for real |
| always_up | 3003 | 46.9 | 49.6 | $-2882.32 | -9.6% | $-1882.32 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4702 | 48.1 | 49.1 | $-2893.72 |
| ETH | 5179 | 48.1 | 48.6 | $-3337.03 |
| SOL | 5410 | 48.0 | 48.6 | $-3207.14 |
| XRP | 5478 | 48.5 | 48.4 | $-2565.42 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
