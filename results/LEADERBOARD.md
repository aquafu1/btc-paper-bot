# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 5:45 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1239 windows, 33751 settled trades, 431 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 663 | 34.2 | 35.3 | $-504.16 | -7.6% | $495.84 | -1.5 | done | can't tell from luck |
| value_ev10 | 1618 | 38.6 | 39.2 | $-840.67 | -5.2% | $159.33 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3385 | 50.8 | 50.2 | $-1101.71 | -3.3% | $-101.71 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2829 | 49.5 | 49.4 | $-1282.87 | -4.5% | $-282.87 | -2.4 | done | losing for real |
| value_ev5 | 2443 | 40.3 | 41.1 | $-1307.46 | -5.4% | $-307.46 | -2.2 | done | losing for real |
| trend_filter | 1995 | 48.8 | 50.4 | $-1673.24 | -8.4% | $-673.24 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2829 | 50.5 | 51.1 | $-1677.96 | -5.9% | $-677.96 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 3385 | 49.2 | 50.2 | $-2085.86 | -6.2% | $-1085.86 | -3.6 | done | losing for real |
| coinflip | 4868 | 50.1 | 50.1 | $-2183.89 | -4.5% | $-1183.89 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 4868 | 50.3 | 51.4 | $-2952.52 | -6.1% | $-1952.52 | -4.4 | done | losing for real |
| always_up | 4868 | 47.9 | 49.3 | $-3559.14 | -7.3% | $-2559.14 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7904 | 48.0 | 48.9 | $-4585.59 |
| ETH | 8537 | 48.1 | 48.3 | $-4999.67 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
