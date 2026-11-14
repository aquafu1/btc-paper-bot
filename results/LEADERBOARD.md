# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 11:50 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 351 windows, 9437 settled trades, 52 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 8:00 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 678 | 41.6 | 42.0 | $-332.85 | -4.9% | $667.15 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 935 | 52.1 | 52.0 | $-378.52 | -4.0% | $621.48 | -1.3 | done | can't tell from luck |
| reversal_60m_0.30pct | 769 | 51.2 | 52.0 | $-414.77 | -5.4% | $585.23 | -1.6 | done | can't tell from luck |
| momentum_60m_0.30pct | 769 | 48.8 | 49.7 | $-474.97 | -6.2% | $525.03 | -1.7 | done | can't tell from luck |
| trend_filter | 520 | 47.7 | 50.3 | $-490.86 | -9.4% | $509.14 | -2.2 | done | losing for real |
| coinflip | 1397 | 50.3 | 50.8 | $-671.57 | -4.8% | $328.43 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 935 | 47.9 | 49.7 | $-711.47 | -7.6% | $288.53 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1397 | 49.2 | 51.4 | $-1117.00 | -8.0% | $-117.00 | -3.1 | done | losing for real |
| always_up | 1397 | 46.6 | 50.6 | $-1623.78 | -11.6% | $-623.78 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2119 | 47.3 | 49.3 | $-1686.47 |
| ETH | 2375 | 47.5 | 48.7 | $-1750.08 |
| SOL | 2445 | 48.1 | 49.4 | $-1797.18 |
| XRP | 2498 | 48.8 | 49.1 | $-1209.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
