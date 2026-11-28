# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 7:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1677 windows, 39674 settled trades, 317 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 848 | 34.2 | 35.2 | $-674.92 | -8.0% | $325.08 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 3894 | 50.8 | 49.9 | $-989.91 | -2.5% | $10.09 | -1.6 | done | can't tell from luck |
| value_ev10 | 2003 | 38.4 | 39.0 | $-1107.13 | -5.5% | $-107.13 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 3249 | 51.1 | 50.9 | $-1416.87 | -4.4% | $-416.87 | -2.5 | done | losing for real |
| value_ev5 | 2989 | 40.3 | 41.0 | $-1612.26 | -5.4% | $-612.26 | -2.5 | done | losing for real |
| momentum_60m_0.30pct | 3249 | 48.9 | 49.3 | $-1831.92 | -5.6% | $-831.92 | -3.2 | done | losing for real |
| trend_filter | 2316 | 48.3 | 50.3 | $-2131.37 | -9.2% | $-1131.37 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3894 | 49.2 | 50.2 | $-2399.41 | -6.2% | $-1399.41 | -3.9 | done | losing for real |
| coinflip | 5744 | 49.9 | 49.9 | $-2493.49 | -4.3% | $-1493.49 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 5744 | 50.2 | 51.3 | $-3563.05 | -6.2% | $-2563.05 | -4.8 | done | losing for real |
| always_up | 5744 | 48.2 | 49.0 | $-3602.14 | -6.3% | $-2602.14 | -4.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10732 | 47.9 | 48.5 | $-6007.73 |
| ETH | 11632 | 47.8 | 47.6 | $-6230.51 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
