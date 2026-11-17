# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 662 windows, 18322 settled trades, 33 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 343 | 34.1 | 35.4 | $-267.49 | -7.8% | $732.51 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1554 | 50.6 | 49.7 | $-371.81 | -2.4% | $628.19 | -0.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1880 | 51.5 | 50.9 | $-550.62 | -2.9% | $449.38 | -1.3 | done | can't tell from luck |
| trend_filter | 1064 | 50.5 | 51.0 | $-565.94 | -5.3% | $434.06 | -1.8 | done | can't tell from luck |
| value_ev10 | 843 | 38.2 | 39.5 | $-621.06 | -7.4% | $378.94 | -1.8 | done | can't tell from luck |
| value_ev5 | 1272 | 40.7 | 41.4 | $-706.42 | -5.6% | $293.58 | -1.7 | done | can't tell from luck |
| coinflip | 2644 | 50.2 | 50.4 | $-1139.91 | -4.3% | $-139.91 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 1554 | 49.4 | 51.3 | $-1266.33 | -8.1% | $-266.33 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 1880 | 48.5 | 50.0 | $-1306.13 | -6.9% | $-306.13 | -3.0 | done | losing for real |
| momentum_5m_0.00pct | 2644 | 50.8 | 51.8 | $-1442.80 | -5.5% | $-442.80 | -2.9 | done | losing for real |
| always_up | 2644 | 47.7 | 49.7 | $-2144.69 | -8.1% | $-1144.69 | -4.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4165 | 48.3 | 49.3 | $-2533.72 |
| ETH | 4570 | 48.2 | 48.7 | $-2857.14 |
| SOL | 4770 | 48.2 | 48.8 | $-2748.89 |
| XRP | 4817 | 48.6 | 48.6 | $-2243.45 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
