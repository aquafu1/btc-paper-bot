# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 350 windows, 9401 settled trades, 60 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 7:15 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 676 | 41.6 | 42.0 | $-330.46 | -4.9% | $669.54 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 930 | 51.9 | 52.0 | $-394.74 | -4.2% | $605.26 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 765 | 51.1 | 52.0 | $-423.38 | -5.5% | $576.62 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 765 | 48.9 | 49.7 | $-452.58 | -5.9% | $547.42 | -1.6 | done | can't tell from luck |
| trend_filter | 519 | 47.6 | 50.3 | $-498.47 | -9.6% | $501.53 | -2.2 | done | losing for real |
| coinflip | 1392 | 50.3 | 50.8 | $-671.84 | -4.8% | $328.16 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 930 | 48.1 | 49.7 | $-679.08 | -7.3% | $320.92 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1392 | 49.0 | 51.4 | $-1150.83 | -8.3% | $-150.83 | -3.2 | done | losing for real |
| always_up | 1392 | 46.4 | 50.6 | $-1657.60 | -11.9% | $-657.60 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2105 | 47.1 | 49.3 | $-1722.56 |
| ETH | 2367 | 47.5 | 48.7 | $-1733.86 |
| SOL | 2438 | 48.0 | 49.3 | $-1808.18 |
| XRP | 2491 | 48.8 | 49.1 | $-1222.21 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
