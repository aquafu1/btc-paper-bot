# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 6:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1194 windows, 32987 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 645 | 34.7 | 35.3 | $-398.79 | -6.2% | $601.21 | -1.2 | done | can't tell from luck |
| value_ev10 | 1572 | 38.5 | 39.2 | $-834.19 | -5.3% | $165.81 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3304 | 50.8 | 50.3 | $-1057.55 | -3.2% | $-57.55 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2767 | 49.6 | 49.4 | $-1238.22 | -4.5% | $-238.22 | -2.3 | done | losing for real |
| value_ev5 | 2377 | 40.3 | 41.1 | $-1322.33 | -5.6% | $-322.33 | -2.3 | done | losing for real |
| trend_filter | 1947 | 48.7 | 50.5 | $-1652.80 | -8.5% | $-652.80 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2767 | 50.4 | 51.1 | $-1686.50 | -6.1% | $-686.50 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3304 | 49.2 | 50.3 | $-2069.66 | -6.3% | $-1069.66 | -3.6 | done | losing for real |
| coinflip | 4768 | 50.1 | 50.1 | $-2122.58 | -4.5% | $-1122.58 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4768 | 50.2 | 51.4 | $-3034.07 | -6.4% | $-2034.07 | -4.5 | done | losing for real |
| always_up | 4768 | 47.8 | 49.3 | $-3517.61 | -7.4% | $-2517.61 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7574 | 48.1 | 48.9 | $-4262.89 |
| ETH | 8181 | 48.0 | 48.4 | $-5083.98 |
| SOL | 8587 | 48.2 | 48.4 | $-4439.94 |
| XRP | 8645 | 48.1 | 48.2 | $-5147.48 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
