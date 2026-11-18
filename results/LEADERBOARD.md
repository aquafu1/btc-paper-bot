# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 12:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 738 windows, 20346 settled trades, 58 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 384 | 33.3 | 34.9 | $-342.66 | -8.9% | $657.34 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2087 | 51.7 | 50.7 | $-457.08 | -2.2% | $542.92 | -1.0 | done | can't tell from luck |
| value_ev10 | 929 | 37.9 | 39.1 | $-636.66 | -6.9% | $363.34 | -1.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 1714 | 49.9 | 49.5 | $-637.14 | -3.7% | $362.86 | -1.5 | done | can't tell from luck |
| value_ev5 | 1403 | 40.5 | 41.1 | $-749.88 | -5.3% | $250.12 | -1.7 | done | can't tell from luck |
| trend_filter | 1196 | 49.9 | 50.9 | $-761.20 | -6.4% | $238.80 | -2.3 | done | losing for real |
| coinflip | 2944 | 50.4 | 50.3 | $-1139.36 | -3.9% | $-139.36 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1714 | 50.1 | 51.3 | $-1193.28 | -7.0% | $-193.28 | -3.0 | done | losing for real |
| momentum_15m_0.10pct | 2087 | 48.3 | 50.1 | $-1527.00 | -7.3% | $-527.00 | -3.4 | done | losing for real |
| momentum_5m_0.00pct | 2944 | 50.8 | 51.8 | $-1603.05 | -5.4% | $-603.05 | -3.1 | done | losing for real |
| always_up | 2944 | 47.0 | 49.6 | $-2709.31 | -9.2% | $-1709.31 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4610 | 48.1 | 49.1 | $-2894.59 |
| ETH | 5073 | 48.1 | 48.6 | $-3213.61 |
| SOL | 5297 | 48.2 | 48.7 | $-3027.07 |
| XRP | 5366 | 48.5 | 48.5 | $-2621.36 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
