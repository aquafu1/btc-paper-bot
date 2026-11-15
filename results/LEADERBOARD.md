# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 6:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 378 windows, 10275 settled trades, 66 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 8:30 PM | too few trades (196/200) |
| value_ev10 | 500 | 40.0 | 40.4 | $-209.12 | -4.2% | $790.88 | -0.8 | done | can't tell from luck |
| value_ev5 | 737 | 41.7 | 42.1 | $-332.45 | -4.5% | $667.55 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 856 | 49.9 | 49.7 | $-346.52 | -4.0% | $653.48 | -1.2 | done | can't tell from luck |
| trend_filter | 568 | 48.9 | 50.4 | $-422.00 | -7.4% | $578.00 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1025 | 51.4 | 52.2 | $-559.57 | -5.5% | $440.43 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1025 | 48.6 | 49.6 | $-577.96 | -5.6% | $422.04 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 856 | 50.1 | 52.1 | $-654.59 | -7.6% | $345.41 | -2.3 | done | losing for real |
| coinflip | 1504 | 49.8 | 50.8 | $-846.64 | -5.6% | $153.36 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1504 | 49.6 | 51.5 | $-1089.49 | -7.2% | $-89.49 | -2.9 | done | losing for real |
| always_up | 1504 | 46.0 | 50.8 | $-1943.02 | -12.9% | $-943.02 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2314 | 47.5 | 49.4 | $-1774.16 |
| ETH | 2584 | 47.6 | 48.8 | $-1830.84 |
| SOL | 2662 | 47.9 | 49.4 | $-1993.55 |
| XRP | 2715 | 48.7 | 49.1 | $-1409.75 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
