# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 28, 2:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1656 windows, 39440 settled trades, 380 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 841 | 34.4 | 35.2 | $-631.08 | -7.5% | $368.92 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3874 | 50.8 | 49.9 | $-1024.04 | -2.6% | $-24.04 | -1.6 | done | can't tell from luck |
| value_ev10 | 1986 | 38.3 | 39.0 | $-1157.41 | -5.8% | $-157.41 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 3242 | 51.1 | 50.9 | $-1436.36 | -4.4% | $-436.36 | -2.6 | done | losing for real |
| value_ev5 | 2965 | 40.3 | 41.0 | $-1640.10 | -5.5% | $-640.10 | -2.6 | done | losing for real |
| momentum_60m_0.30pct | 3242 | 48.9 | 49.2 | $-1822.51 | -5.6% | $-822.51 | -3.2 | done | losing for real |
| trend_filter | 2310 | 48.3 | 50.4 | $-2134.47 | -9.2% | $-1134.47 | -4.5 | done | losing for real |
| momentum_15m_0.10pct | 3874 | 49.2 | 50.2 | $-2358.00 | -6.1% | $-1358.00 | -3.8 | done | losing for real |
| coinflip | 5702 | 49.9 | 49.9 | $-2521.55 | -4.4% | $-1521.55 | -3.3 | done | losing for real |
| always_up | 5702 | 48.3 | 49.0 | $-3521.48 | -6.2% | $-2521.48 | -4.6 | done | losing for real |
| momentum_5m_0.00pct | 5702 | 50.2 | 51.3 | $-3536.75 | -6.2% | $-2536.75 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 10622 | 47.9 | 48.5 | $-6040.07 |
| ETH | 11508 | 47.9 | 47.6 | $-6159.45 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
