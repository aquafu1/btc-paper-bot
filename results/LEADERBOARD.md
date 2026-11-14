# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 3:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 366 windows, 9878 settled trades, 74 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:00 PM | too few trades (189/200) |
| value_ev10 | 478 | 41.2 | 40.3 | $-52.64 | -1.1% | $947.36 | -0.2 | done | can't tell from luck |
| value_ev5 | 707 | 42.4 | 42.0 | $-178.96 | -2.5% | $821.04 | -0.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 813 | 49.6 | 49.7 | $-368.39 | -4.5% | $631.61 | -1.3 | done | can't tell from luck |
| trend_filter | 548 | 48.9 | 50.5 | $-402.24 | -7.3% | $597.76 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 981 | 51.5 | 52.1 | $-501.61 | -5.1% | $498.39 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 981 | 48.5 | 49.6 | $-555.82 | -5.7% | $444.18 | -1.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 813 | 50.4 | 52.1 | $-557.12 | -6.9% | $442.88 | -2.0 | done | losing for real |
| coinflip | 1456 | 50.0 | 50.8 | $-748.90 | -5.1% | $251.10 | -2.0 | done | can't tell from luck |
| momentum_5m_0.00pct | 1456 | 49.5 | 51.6 | $-1063.79 | -7.3% | $-63.79 | -2.9 | done | losing for real |
| always_up | 1456 | 45.6 | 50.7 | $-1967.41 | -13.5% | $-967.41 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2219 | 47.3 | 49.3 | $-1743.31 |
| ETH | 2484 | 47.7 | 48.8 | $-1695.98 |
| SOL | 2560 | 48.1 | 49.4 | $-1747.30 |
| XRP | 2615 | 48.9 | 49.1 | $-1194.52 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
