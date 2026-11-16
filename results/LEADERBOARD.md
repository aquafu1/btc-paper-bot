# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 11:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 541 windows, 14979 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1281 | 51.5 | 49.8 | $-153.11 | -1.2% | $846.89 | -0.4 | done | can't tell from luck |
| value_ev20 | 287 | 33.8 | 35.5 | $-282.64 | -9.8% | $717.36 | -1.3 | done | can't tell from luck |
| trend_filter | 871 | 50.6 | 50.9 | $-426.33 | -4.9% | $573.67 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1520 | 49.7 | 49.7 | $-670.49 | -4.4% | $329.51 | -1.7 | done | can't tell from luck |
| value_ev10 | 703 | 37.3 | 39.7 | $-710.63 | -10.1% | $289.37 | -2.2 | done | losing for real |
| value_ev5 | 1048 | 39.4 | 41.4 | $-936.07 | -8.9% | $63.93 | -2.5 | done | losing for real |
| reversal_15m_0.10pct | 1520 | 50.3 | 51.3 | $-1054.79 | -6.9% | $-54.79 | -2.8 | done | losing for real |
| coinflip | 2156 | 49.9 | 50.6 | $-1235.31 | -5.7% | $-235.31 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1281 | 48.5 | 51.3 | $-1310.02 | -10.2% | $-310.02 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2156 | 50.0 | 51.7 | $-1553.52 | -7.2% | $-553.52 | -3.5 | done | losing for real |
| always_up | 2156 | 46.7 | 50.1 | $-2430.20 | -11.3% | $-1430.20 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3395 | 47.5 | 49.2 | $-2770.90 |
| ETH | 3738 | 48.0 | 48.7 | $-2589.81 |
| SOL | 3907 | 47.6 | 48.9 | $-3054.77 |
| XRP | 3939 | 48.5 | 48.8 | $-2347.64 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
