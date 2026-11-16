# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 549 windows, 15241 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1305 | 51.4 | 49.7 | $-208.15 | -1.6% | $791.85 | -0.6 | done | can't tell from luck |
| value_ev20 | 300 | 33.0 | 35.2 | $-354.01 | -11.8% | $645.99 | -1.6 | done | can't tell from luck |
| trend_filter | 888 | 50.7 | 51.0 | $-459.63 | -5.2% | $540.37 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1542 | 49.7 | 49.8 | $-701.16 | -4.5% | $298.84 | -1.8 | done | can't tell from luck |
| value_ev10 | 720 | 36.8 | 39.4 | $-801.10 | -11.1% | $198.90 | -2.5 | done | losing for real |
| value_ev5 | 1072 | 39.3 | 41.2 | $-978.33 | -9.1% | $21.67 | -2.6 | done | losing for real |
| reversal_15m_0.10pct | 1542 | 50.3 | 51.2 | $-1060.61 | -6.9% | $-60.61 | -2.8 | done | losing for real |
| coinflip | 2189 | 49.9 | 50.5 | $-1277.50 | -5.8% | $-277.50 | -2.8 | done | losing for real |
| reversal_60m_0.30pct | 1305 | 48.6 | 51.2 | $-1328.51 | -10.2% | $-328.51 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 2189 | 50.2 | 51.8 | $-1595.20 | -7.3% | $-595.20 | -3.6 | done | losing for real |
| always_up | 2189 | 46.8 | 50.0 | $-2423.04 | -11.1% | $-1423.04 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3446 | 47.4 | 49.2 | $-2848.91 |
| ETH | 3799 | 47.9 | 48.6 | $-2762.88 |
| SOL | 3975 | 47.7 | 48.7 | $-3084.54 |
| XRP | 4021 | 48.4 | 48.6 | $-2490.93 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
