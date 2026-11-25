# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 4:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1427 windows, 36483 settled trades, 444 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 734 | 34.6 | 35.3 | $-505.63 | -6.9% | $494.37 | -1.4 | done | can't tell from luck |
| value_ev10 | 1772 | 38.8 | 39.1 | $-793.63 | -4.5% | $206.37 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3643 | 50.8 | 50.1 | $-1033.47 | -2.8% | $-33.47 | -1.7 | done | can't tell from luck |
| value_ev5 | 2673 | 40.6 | 41.1 | $-1268.07 | -4.7% | $-268.07 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3060 | 49.2 | 49.3 | $-1508.56 | -4.9% | $-508.56 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3060 | 50.8 | 51.0 | $-1559.38 | -5.1% | $-559.38 | -2.9 | done | losing for real |
| trend_filter | 2166 | 48.6 | 50.3 | $-1885.16 | -8.7% | $-885.16 | -4.1 | done | losing for real |
| coinflip | 5244 | 50.1 | 50.0 | $-2229.80 | -4.3% | $-1229.80 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3643 | 49.2 | 50.2 | $-2235.49 | -6.1% | $-1235.49 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 5244 | 50.2 | 51.3 | $-3242.39 | -6.2% | $-2242.39 | -4.6 | done | losing for real |
| always_up | 5244 | 47.9 | 49.3 | $-3675.55 | -7.0% | $-2675.55 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9240 | 48.1 | 48.7 | $-4959.66 |
| ETH | 9933 | 48.0 | 48.0 | $-5393.24 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
