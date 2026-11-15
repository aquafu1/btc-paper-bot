# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 394 windows, 10786 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 197 | 37.1 | 36.6 | $-36.95 | -1.9% | $963.05 | -0.2 | Sun 12:00 AM | too few trades (197/200) |
| value_ev10 | 513 | 40.5 | 40.5 | $-155.67 | -3.0% | $844.33 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 914 | 50.7 | 49.8 | $-212.94 | -2.3% | $787.06 | -0.7 | done | can't tell from luck |
| value_ev5 | 760 | 42.1 | 42.2 | $-271.20 | -3.6% | $728.80 | -0.8 | done | can't tell from luck |
| trend_filter | 612 | 49.7 | 50.5 | $-346.21 | -5.7% | $653.79 | -1.4 | done | can't tell from luck |
| momentum_15m_0.10pct | 1086 | 49.0 | 49.7 | $-536.57 | -4.9% | $463.43 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1086 | 51.0 | 52.1 | $-630.37 | -5.8% | $369.63 | -2.0 | done | losing for real |
| reversal_60m_0.30pct | 914 | 49.3 | 52.1 | $-820.27 | -9.0% | $179.73 | -2.8 | done | losing for real |
| coinflip | 1568 | 49.9 | 50.8 | $-846.00 | -5.4% | $154.00 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1568 | 49.8 | 51.6 | $-1056.87 | -6.7% | $-56.87 | -2.8 | done | losing for real |
| always_up | 1568 | 46.4 | 50.7 | $-1854.97 | -11.8% | $-854.97 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2440 | 47.7 | 49.5 | $-1660.40 |
| ETH | 2712 | 48.0 | 48.9 | $-1644.89 |
| SOL | 2789 | 48.0 | 49.5 | $-2050.44 |
| XRP | 2845 | 48.9 | 49.2 | $-1412.30 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
