# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 11:15 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 493 windows, 13554 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 251 | 34.3 | 35.8 | $-189.21 | -7.5% | $810.79 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1150 | 51.0 | 49.9 | $-209.00 | -1.8% | $791.00 | -0.6 | done | can't tell from luck |
| value_ev10 | 639 | 38.3 | 40.0 | $-470.56 | -7.4% | $529.44 | -1.5 | done | can't tell from luck |
| trend_filter | 794 | 49.7 | 50.8 | $-513.07 | -6.5% | $486.93 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1367 | 49.9 | 49.9 | $-514.47 | -3.8% | $485.53 | -1.4 | done | can't tell from luck |
| value_ev5 | 944 | 40.6 | 41.7 | $-586.78 | -6.2% | $413.22 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1367 | 50.1 | 51.5 | $-931.24 | -6.8% | $68.76 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1150 | 49.0 | 51.4 | $-1039.80 | -9.0% | $-39.80 | -3.1 | done | losing for real |
| coinflip | 1964 | 49.9 | 50.7 | $-1051.63 | -5.4% | $-51.63 | -2.4 | done | losing for real |
| momentum_5m_0.00pct | 1964 | 49.8 | 51.7 | $-1400.85 | -7.1% | $-400.85 | -3.3 | done | losing for real |
| always_up | 1964 | 46.3 | 50.3 | $-2303.00 | -11.7% | $-1303.00 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3054 | 47.4 | 49.3 | $-2467.90 |
| ETH | 3396 | 48.0 | 48.8 | $-2212.80 |
| SOL | 3538 | 47.8 | 49.2 | $-2573.07 |
| XRP | 3566 | 48.4 | 48.9 | $-1955.83 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
