# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 12:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 592 windows, 16379 settled trades, 50 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1388 | 51.2 | 49.6 | $-219.29 | -1.6% | $780.71 | -0.6 | done | can't tell from luck |
| value_ev20 | 322 | 34.2 | 35.2 | $-257.97 | -8.0% | $742.03 | -1.1 | done | can't tell from luck |
| trend_filter | 950 | 50.1 | 51.0 | $-564.37 | -5.9% | $435.63 | -1.9 | done | can't tell from luck |
| value_ev10 | 770 | 37.8 | 39.4 | $-636.74 | -8.3% | $363.26 | -1.9 | done | can't tell from luck |
| value_ev5 | 1151 | 40.4 | 41.2 | $-713.04 | -6.2% | $286.96 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1665 | 51.1 | 51.0 | $-721.37 | -4.3% | $278.63 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1665 | 48.9 | 49.9 | $-1009.40 | -6.1% | $-9.40 | -2.5 | done | losing for real |
| coinflip | 2360 | 49.9 | 50.5 | $-1235.41 | -5.2% | $-235.41 | -2.6 | done | losing for real |
| reversal_60m_0.30pct | 1388 | 48.8 | 51.3 | $-1331.93 | -9.6% | $-331.93 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2360 | 50.1 | 51.8 | $-1641.32 | -7.0% | $-641.32 | -3.5 | done | losing for real |
| always_up | 2360 | 47.4 | 49.8 | $-2116.92 | -9.0% | $-1116.92 | -4.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3715 | 47.9 | 49.2 | $-2579.77 |
| ETH | 4086 | 48.0 | 48.5 | $-2632.49 |
| SOL | 4259 | 47.9 | 48.7 | $-2989.95 |
| XRP | 4319 | 48.5 | 48.6 | $-2245.55 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
