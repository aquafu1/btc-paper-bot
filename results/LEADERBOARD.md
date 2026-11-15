# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 380 windows, 10341 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 9:00 PM | too few trades (196/200) |
| value_ev10 | 503 | 40.0 | 40.5 | $-217.29 | -4.3% | $782.71 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 863 | 49.8 | 49.7 | $-354.38 | -4.1% | $645.62 | -1.2 | done | can't tell from luck |
| value_ev5 | 742 | 41.5 | 42.1 | $-360.61 | -4.9% | $639.39 | -1.1 | done | can't tell from luck |
| trend_filter | 572 | 48.6 | 50.4 | $-462.00 | -8.1% | $538.00 | -2.0 | done | can't tell from luck |
| reversal_15m_0.10pct | 1033 | 51.7 | 52.2 | $-507.16 | -4.9% | $492.84 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1033 | 48.3 | 49.6 | $-640.65 | -6.2% | $359.35 | -2.0 | done | can't tell from luck |
| reversal_60m_0.30pct | 863 | 50.2 | 52.1 | $-654.32 | -7.6% | $345.68 | -2.3 | done | losing for real |
| coinflip | 1512 | 49.8 | 50.8 | $-849.57 | -5.6% | $150.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1512 | 49.4 | 51.5 | $-1152.18 | -7.6% | $-152.18 | -3.1 | done | losing for real |
| always_up | 1512 | 46.0 | 50.7 | $-1960.88 | -13.0% | $-960.88 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2329 | 47.4 | 49.4 | $-1828.09 |
| ETH | 2600 | 47.6 | 48.9 | $-1880.49 |
| SOL | 2678 | 47.9 | 49.4 | $-2019.25 |
| XRP | 2734 | 48.6 | 49.1 | $-1458.17 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
