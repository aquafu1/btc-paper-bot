# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 8:30 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1442 windows, 36683 settled trades, 403 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 740 | 34.5 | 35.3 | $-533.47 | -7.2% | $466.53 | -1.5 | done | can't tell from luck |
| value_ev10 | 1784 | 38.8 | 39.2 | $-786.32 | -4.4% | $213.68 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 3662 | 50.9 | 50.0 | $-981.56 | -2.7% | $18.44 | -1.6 | done | can't tell from luck |
| value_ev5 | 2687 | 40.6 | 41.1 | $-1280.77 | -4.8% | $-280.77 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3075 | 49.2 | 49.2 | $-1509.80 | -4.9% | $-509.80 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3075 | 50.8 | 51.0 | $-1580.64 | -5.1% | $-580.64 | -2.9 | done | losing for real |
| trend_filter | 2176 | 48.6 | 50.3 | $-1877.44 | -8.6% | $-877.44 | -4.1 | done | losing for real |
| coinflip | 5274 | 50.0 | 50.0 | $-2240.81 | -4.2% | $-1240.81 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3662 | 49.1 | 50.2 | $-2272.22 | -6.2% | $-1272.22 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5274 | 50.2 | 51.3 | $-3265.03 | -6.2% | $-2265.03 | -4.6 | done | losing for real |
| always_up | 5274 | 48.0 | 49.2 | $-3562.98 | -6.8% | $-2562.98 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9338 | 48.1 | 48.7 | $-4883.31 |
| ETH | 10035 | 48.0 | 48.0 | $-5423.49 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
