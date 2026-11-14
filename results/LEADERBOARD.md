# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 348 windows, 9344 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:45 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 675 | 41.6 | 42.0 | $-320.46 | -4.7% | $679.54 | -1.1 | done | can't tell from luck |
| reversal_60m_0.30pct | 757 | 51.7 | 52.1 | $-343.38 | -4.5% | $656.62 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 926 | 51.9 | 52.0 | $-391.60 | -4.2% | $608.40 | -1.4 | done | can't tell from luck |
| momentum_60m_0.30pct | 757 | 48.3 | 49.6 | $-502.71 | -6.6% | $497.29 | -1.8 | done | can't tell from luck |
| trend_filter | 511 | 46.8 | 50.2 | $-548.60 | -10.7% | $451.40 | -2.5 | done | losing for real |
| coinflip | 1384 | 50.3 | 50.8 | $-657.85 | -4.8% | $342.15 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 926 | 48.1 | 49.7 | $-669.25 | -7.2% | $330.75 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1384 | 48.7 | 51.3 | $-1200.96 | -8.7% | $-200.96 | -3.3 | done | losing for real |
| always_up | 1384 | 46.7 | 50.6 | $-1577.60 | -11.4% | $-577.60 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2093 | 47.0 | 49.3 | $-1732.30 |
| ETH | 2353 | 47.5 | 48.7 | $-1714.63 |
| SOL | 2422 | 47.9 | 49.3 | $-1816.06 |
| XRP | 2476 | 48.8 | 49.1 | $-1177.26 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
