# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 452 windows, 12402 settled trades, 47 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1052 | 51.2 | 50.0 | $-199.67 | -1.9% | $800.33 | -0.6 | done | can't tell from luck |
| value_ev10 | 585 | 38.8 | 40.1 | $-391.01 | -6.7% | $608.99 | -1.3 | done | can't tell from luck |
| trend_filter | 715 | 49.9 | 50.7 | $-397.75 | -5.6% | $602.25 | -1.5 | done | can't tell from luck |
| value_ev5 | 867 | 40.9 | 41.9 | $-505.69 | -5.8% | $494.31 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1252 | 49.6 | 50.0 | $-554.54 | -4.4% | $445.46 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1252 | 50.4 | 51.6 | $-832.72 | -6.7% | $167.28 | -2.5 | done | losing for real |
| coinflip | 1800 | 49.8 | 50.8 | $-1043.19 | -5.8% | $-43.19 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1052 | 48.8 | 51.7 | $-1050.01 | -10.0% | $-50.01 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 1800 | 49.6 | 51.5 | $-1322.97 | -7.3% | $-322.97 | -3.2 | done | losing for real |
| always_up | 1800 | 45.8 | 50.6 | $-2365.82 | -13.1% | $-1365.82 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2800 | 47.5 | 49.3 | $-2252.29 |
| ETH | 3117 | 47.9 | 48.8 | $-2118.44 |
| SOL | 3226 | 47.6 | 49.3 | $-2542.43 |
| XRP | 3259 | 48.4 | 49.2 | $-1902.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
