# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 12:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 352 windows, 9461 settled trades, 67 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 8:00 PM | too few trades (184/200) |
| value_ev10 | 456 | 40.1 | 40.3 | $-189.48 | -4.2% | $810.52 | -0.7 | done | can't tell from luck |
| value_ev5 | 678 | 41.6 | 42.0 | $-332.85 | -4.9% | $667.15 | -1.1 | done | can't tell from luck |
| reversal_15m_0.10pct | 938 | 51.9 | 52.0 | $-408.52 | -4.4% | $591.48 | -1.4 | done | can't tell from luck |
| reversal_60m_0.30pct | 772 | 51.0 | 52.0 | $-444.77 | -5.8% | $555.23 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 772 | 49.0 | 49.7 | $-454.12 | -5.9% | $545.88 | -1.6 | done | can't tell from luck |
| trend_filter | 523 | 48.0 | 50.4 | $-470.01 | -9.0% | $529.99 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 938 | 48.1 | 49.8 | $-690.62 | -7.4% | $309.38 | -2.3 | done | losing for real |
| coinflip | 1400 | 50.2 | 50.8 | $-701.57 | -5.0% | $298.43 | -1.9 | done | can't tell from luck |
| momentum_5m_0.00pct | 1400 | 49.3 | 51.4 | $-1096.15 | -7.8% | $-96.15 | -3.0 | done | losing for real |
| always_up | 1400 | 46.7 | 50.6 | $-1602.93 | -11.4% | $-602.93 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2119 | 47.3 | 49.3 | $-1686.47 |
| ETH | 2383 | 47.6 | 48.7 | $-1744.59 |
| SOL | 2453 | 48.1 | 49.4 | $-1792.10 |
| XRP | 2506 | 48.9 | 49.1 | $-1206.22 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
